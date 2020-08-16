# weewx-skin-2json

A [weewx](https://github.com/weewx/weewx) skin to export JSON for single page application (SPA) usage.


## Installation

1. Download the source zip:
    ```shell script
    wget -O /tmp/weewx-skin-2json.zip https://github.com/WorkingDevel/weewx-skin-2json/archive/master.zip
    ```
2. Install via `wee_extension`
    ```shell script
    wee_extension --install=/tmp/weewx-skin-2json.zip
    ```

## Uninstall

Just use the `wee_extension` executable again:
```shell script
wee_extension --uninstall=2Json
```
