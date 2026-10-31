import { Config } from "@remotion/cli/config";

// Long videos: H.264, CRF 18. 4K masters: add --scale=2 on the command line.
Config.setVideoImageFormat("jpeg");
Config.setCodec("h264");
Config.setCrf(18);
Config.setOverwriteOutput(true);
// Sound effects, music and narration live in audio/ (use staticFile("sfx/ding.wav")).
Config.setPublicDir("audio");
// Concurrency is passed per render (--concurrency=4 on the owner's PC; lower it if RAM goes above
// ~13 GB). It is not set here because Remotion errors on machines with fewer cores.
