# ricemgr
## Command Structure
```
ricemgr/
├── file/
│   ├── add/
│   │   └── <file>
│   ├── list/
│   ├── sync/
│   │   └── <file> / all
│   └── remove/
│       └── <file> / all
├── package/
│   ├── add/
│   │   ├── <package>
│   │   └── optional: -v --version
│   ├── list/
│   ├── sync/
│   │   └── <package> / all
│   ├── edit/
│   └── remove/
│       └── <package> / all
├── profile/
│   ├── new/
│   │   └── <name>
│   ├── list/
│   │   └── <profile> / default: current profile
│   ├── sync/
│   ├── rename/
│   │   └── <name>
│   ├── edit/
│   │   └── <config file> / **add more detailed list later**
│   ├── delete/
│   │   └── <profile>
│   ├── switch/
│   │   └── <profile>
│   ├── export/
│   │   └── <file> / default: current profile name
│   └── import/
│       └── <file>
├── init/
└── clean/
```

## Requirements
- Rice file tracking
  - Dotfiles/Required Files(i.e. background images)
    - [ ] Add dotfile/required file to profile
      - [x] Keep file paths user-agnostic
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
  - [ ] Rename profiles
  - [ ] Delete rice profiles
  - [ ] List profiles
  - [ ] Switch rice profiles
    - [ ] Restart software that needs to be restarted
    - [ ] Ask the user to restart when required
  - [ ] Export a complete rice profile(to *.rice)
  - [ ] Import a complete rice profile(from *.rice)
    - [ ] Check for missing package requirements
    - [ ] Rename duplicate names
- [ ] XDG Compliant
- OS Support(this includes managing rice-related packages)
  - [ ] Arch + Derivatives
  - [ ] Ubuntu + Derivatives
  - [ ] Mac
- UI
  - [x] CLI
  - [ ] TUI/GUI
- Scripting and Event System
  - [ ] Add script to profile
  - [ ] Remove script from profile
  - [ ] List scripts in profile
  - [ ] Execute custom scripts
  - [ ] Run scripts based on internal events
- Version Control
