# silent-writing-theme

A silenced theme in a black & white palette.

![demo](https://raw.githubusercontent.com/seppzer0/silent-writing-theme/main/assets/demo.png)

## Inspiration

I was fond of a basic scheme with a black background and white text. This colour combination felt simplistic yet elegant, which made me curious to try adapting it for my coding environment.

I have tried several existing solutions, with none feeling quite right. There were still some elements that were either eye-razoring or otherwise distracting from a thought process, which reallistically is the only thing that matters when writing code. I could just start coding in terminals exclusively; but I didn't want to leave VSCode just yet.

This version of white-on-black theme is intended to be balanced. I thought maybe my bland taste in colours might be shared by someone else, so I decided to make it publicly available for everyone to try it.

## Availability

This colour theme is available in Microsoft's Marketplace and [GitHub Releases](https://github.com/seppzer0/silent-writing-theme/releases).

## Installation

### IDE (recommended)

In the `Extensions` menu of your VSCode installation search for "Silent Writing Theme" extension. Once found, click the "Install" button.

### VSIX

You can download a .vsix file from the release page and install it directly.

Below is an example of doing so via a command line:

```sh
code --install-extentions <path_to_vsix_file>
```

For VSCodium, use `codium` command instead.

### Git (for Development and Testing)

In case you want to modify this theme yourself, you can copy it as a git repository:

```sh
git clone https://github.com/seppzer0/silent-writing-theme ~/.vscode/extensions/silent-writing-theme
```

For VSCodium, use `~/.vscode-oss/extensions/silent-writing-theme` path instead.

## Acknowledgments

- [obsidian-minimal](https://github.com/kepano/obsidian-minimal): Obsidian theme inspiring the idea;
- [vscode-pitch-black-theme](https://github.com/ViktorQvarfordt/vscode-pitch-black-theme): Starting base of the project.

## License

[MIT](https://github.com/seppzer0/silent-writing-theme/blob/main/LICENSE.md)
