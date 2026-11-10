# Overnight render-queue supervisor: restarts scripts/episode_pipeline.mts if it
# exits early (e.g. an OOM kill), as long as each attempt makes progress (the
# render-queue.log grows). Stops after 3 consecutive no-progress restarts, when
# the pipeline finishes on its own (exit code 0), when it stops deliberately
# after 2 consecutive episode failures (exit code 2 - not retried, since that's
# a quality signal to look at, not a crash), or past the 05:30 time-box (which
# episode_pipeline.mts also enforces internally, per-episode).
#
# Usage: powershell -File scripts/overnight.ps1 -StartEp 5 -EndEp 19

param(
    [Parameter(Mandatory = $true)][int]$StartEp,
    [Parameter(Mandatory = $true)][int]$EndEp,
    [switch]$NoTimebox
)

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$logPath = Join-Path $root "out\render-queue.log"
$supervisorLog = Join-Path $root "out\overnight-supervisor.log"

function Write-SupervisorLog($msg) {
    $line = "$(Get-Date -Format o) $msg"
    Add-Content -Path $supervisorLog -Value $line
    Write-Host $line
}

function Get-LogSize {
    if (Test-Path $logPath) { return (Get-Item $logPath).Length }
    return 0
}

function Past-Cutoff {
    if ($NoTimebox) { return $false }  # actively supervised right now, not unattended overnight
    $now = Get-Date
    $cutoff = Get-Date -Hour 5 -Minute 30 -Second 0
    # Before midnight (e.g. started at 21:00), "now" > "today's 05:30" is
    # true but we have NOT crossed the actual cutoff yet - only treat it as
    # past cutoff once the hour is in the early-morning window (0-5).
    if ($now.Hour -ge 6 -and $now.Hour -le 23) { return $false }
    return $now -ge $cutoff
}

$noProgressCount = 0
$maxNoProgressRestarts = 3

Write-SupervisorLog "Overnight supervisor starting: ep$StartEp..ep$EndEp"

# Preflight: list scenes that would render blank or crash. episode_pipeline.mts skips those episodes.
& node scripts/check_scenes.mts $StartEp $EndEp | ForEach-Object { Write-SupervisorLog $_ }

while ($true) {
    if (Past-Cutoff) {
        Write-SupervisorLog "Past 05:30 time-box, stopping supervisor."
        break
    }

    $beforeSize = Get-LogSize
    Write-SupervisorLog "Launching episode_pipeline.mts $StartEp $EndEp (log size before: $beforeSize)"

    if ($NoTimebox) {
        & node scripts/episode_pipeline.mts $StartEp $EndEp --no-timebox
    } else {
        & node scripts/episode_pipeline.mts $StartEp $EndEp
    }
    $exitCode = $LASTEXITCODE

    $afterSize = Get-LogSize
    Write-SupervisorLog "episode_pipeline.mts exited with code $exitCode (log size after: $afterSize)"

    if ($exitCode -eq 0) {
        Write-SupervisorLog "Pipeline finished cleanly. Supervisor done."
        break
    }

    if ($exitCode -eq 2) {
        Write-SupervisorLog "Pipeline stopped deliberately (2 consecutive episode failures) - not a crash, not retrying. Supervisor done."
        break
    }

    if ($afterSize -gt $beforeSize) {
        Write-SupervisorLog "Progress was made since last attempt; resetting no-progress counter."
        $noProgressCount = 0
    } else {
        $noProgressCount++
        Write-SupervisorLog "No progress this attempt. no-progress count = $noProgressCount / $maxNoProgressRestarts"
        if ($noProgressCount -ge $maxNoProgressRestarts) {
            Write-SupervisorLog "No progress after $maxNoProgressRestarts restarts in a row. Stopping."
            break
        }
    }

    Start-Sleep -Seconds 15
}

Write-SupervisorLog "Overnight supervisor exiting."
