<#
Prepares a Shorts-only re-render: MOVES (never deletes) out\epNNN\epNNN-S1..S5.mp4 into out\old-shorts-<Tag>\epNNN\,
so scripts/episode_pipeline.mts finds the long 4K video present (3840x2160, it is SKIPPED) and renders only the missing Shorts,
then redoes the QA. Throws if the destination folder already exists. Run it BEFORE overnight.ps1, in your own PowerShell.
  powershell -NoProfile -File scripts/prep_shorts_rerender.ps1 -StartEp 41 -EndEp 50 -Tag 2026-11-06
#>
param(
    [Parameter(Mandatory = $true)][int]$StartEp,
    [Parameter(Mandatory = $true)][int]$EndEp,
    [Parameter(Mandatory = $true)][string]$Tag
)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$dest = Join-Path $root "out\old-shorts-$Tag"
if (Test-Path $dest) { throw "$dest already exists" }
New-Item -ItemType Directory $dest | Out-Null
$moved = 0
foreach ($ep in $StartEp..$EndEp) {
    $id = 'ep{0:000}' -f $ep
    $src = Join-Path $root "out\$id"
    if (-not (Test-Path (Join-Path $src "$id-4k.mp4"))) { throw "$id has no long 4K video: a Shorts-only run would render it in full" }
    $to = Join-Path $dest $id
    New-Item -ItemType Directory $to | Out-Null
    foreach ($s in 1..5) {
        $f = Join-Path $src "$id-S$s.mp4"
        if (Test-Path $f) { Move-Item $f $to; $moved++ }
    }
}
Write-Host "Moved $moved Shorts to $dest. Now run: powershell -NoProfile -File scripts/overnight.ps1 -StartEp $StartEp -EndEp $EndEp -NoTimebox"
