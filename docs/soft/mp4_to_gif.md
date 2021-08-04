title: mp4 to gif

## Команды для создания гифки из видео с помощью ffmpeg

```shell
## Сделать превью
ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
## Сделать гифку на всю длину видео
ffmpeg -i input.mp4 -vf "fps=10,scale=-1:1024:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```