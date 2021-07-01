# scripts
Useful scripts in one place


## Map Graphics tablet to one monitor

Find the Tablet Pen input
```sh
$ xinput
```

Get the monitor list

```sh
$ xrandr
```

Map the output:

```sh
$ xinput --map-to-output <id> <monitor-id>
```

Example:

```sh
$ xinput --map-to-output 15 "HDMI-1"
```
