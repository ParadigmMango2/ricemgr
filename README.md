# ricemgr
## Command Structure
```
ricemgr/
├── file/
│   ├── add/
│   │   └── <file>
│   ├── list/
│   ├── delete/
│   │   └── <file> / all
│   └── sync/
│       └── <file> / all
├── package/
│   ├── add/
│   │   ├── <package>
│   │   └── optional: -v --version
│   ├── list/
│   ├── remove/
│   │   └── <package> / all
│   ├── edit/
│   └── sync/
│       └── <package> / all
└── profile/
    ├── new/
    │   └── <name>
    ├── delete/
    │   └── <profile>
    ├── list/
    │   └── <profile> / default: current profile
    ├── sync/
    │   ├── <profile> / default: current profile
    │   └── optional: all
    ├── edit/
    │   └── <config file> / **add more detailed list later**
    ├── switch/
    │   └── <profile>
    ├── export/
    │   └── <file> / default: current profile name
    └── import/
        └── <file>
```

## Requirements
- Rice file tracking
  - Dotfiles/Required Files(i.e. background images)
    - [ ] Add dotfile/required file to profile
      - [ ] Keep file paths user-agnostic
    - [ ] Remove dotfile/required file from profile
    - [ ] List dotfiles in profile
    - [ ] Keep local copies of the most up-to-date dotfiles/required files
      - [ ] Manually update file
      - [ ] Automatically update file
  - Track Required Software
    - [ ] Add software to required list
    - [ ] Remove software from required list
    - [ ] List required software
    - [ ] Track minimum versions (by default, do not track)
      - [ ] Update minimum version number
    - [ ] Required software checking
    - [ ] Create required software list
      - [ ] Manually update software list
      - [ ] Automatically update software list
- Rice Profiles
  - [ ] Make new rice profile
  - [ ] Delete rice profile
  - [ ] List profiles
  - [ ] Switch rice profiles
    - [ ] Restart software that needs to be restarted
    - [ ] Ask the user to restart when required
  - [ ] Export a complete rice profile(to *.rice)
  - [ ] Import a complete rice profile(from *.rice)
    - [ ] Check for missing package requirements
- [ ] XDG Compliant
- OS Support(this includes managing rice-related packages)
  - [ ] Arch + Derivatives
  - [ ] Ubuntu + Derivatives
  - [ ] Mac
- UI
  - [ ] CLI
  - [ ] TUI/GUI
- Scripting and Event System
  - [ ] Add script to profile
  - [ ] Remove script from profile
  - [ ] List scripts in profile
  - [ ] Execute custom scripts
  - [ ] Run scripts based on internal events
- Version Control
