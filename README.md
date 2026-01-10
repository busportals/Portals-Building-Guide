# Portals Building Guide

Welcome to the Portals Building Guide — the official docs for creating browser-based games and interactive spaces in [Portals](https://theportal.to).

If you're new, start with the basics. If you're experienced, jump straight to advanced tooling and patterns.

## Start Here

- **New to Portals:** [Creating a Space](building-basics/getting-started/creating-a-space.md)
- **Want an overview of the editor:** [Interactive Studio](interactive-studio/overview.md)
- **Ready for deeper systems:** [Advanced Tooling](advanced-tooling/function-effect/README.md)
- **Prefer step-by-step recipes:** [How To](how-to/create-a-basic-token-trading-space.md)
- **Building events and challenges:** [Building Competitions](building-competitions/december-2025-christmas-building-competition.md)

## Live Documentation

Read the live docs here: https://prtls.gitbook.io/portals-building-guide

---

# Claude Code Skill

This repository also includes a **Claude Code skill** that teaches AI assistants everything about Portals building.

## Install the Skill

### Quick Install (Recommended)

```bash
npx skills-installer install @busportals/Portals-Building-Guide/portals-building-guide --client claude-code
```

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/busportals/Portals-Building-Guide.git
```

2. Copy the skill to your Claude Code skills directory:

**Windows:**
```bash
xcopy /E /I "Portals-Building-Guide\skills\portals-building-guide" "%USERPROFILE%\.claude\skills\portals-building-guide"
```

**macOS/Linux:**
```bash
cp -r Portals-Building-Guide/skills/portals-building-guide ~/.claude/skills/
```

3. Restart Claude Code to load the skill.

### Verify Installation

```bash
npx skills-installer list
```

You should see `portals-building-guide` in the list.

## What the Skill Includes

The skill teaches Claude everything about building in Portals:

| Category | Coverage |
|----------|----------|
| **Building Basics** | Creating spaces, build mode, all 20 building tools |
| **Interactive Studio** | Tasks (3 states), 14 triggers, 60+ effects |
| **Function Effect** | NCalc scripting, operators, conditions |
| **Advanced Features** | Quests, NPCs, iframes, token trading, variables |

## Usage Examples

Once installed, ask Claude about Portals building:

```
"How do I create a door that opens when clicked?"
"Set up a quest system with 3 tasks"
"Write a function effect that gives coins when health drops"
"Configure an NPC with dialogue"
"Create a token trading space"
```

## Quick Reference

### Task State Syntax
```
$T{taskName}     -> Returns 'NotActive', 'Active', or 'Completed'
$TN{taskName}    -> Returns 0, 1, or 2
$N{variableName} -> Returns numeric value
```

### Setting Values
```
SetTask('door', 'Active', 0.0)           // Immediate
SetTask('alarm', 'NotActive', 5.0)       // 5-second delay
SetVariable('coins', $N{coins} + 10, 0.0)
```

### Conditions
```
if($N{coins} >= 10,
   SetVariable('doorUnlocked', 1, 0.0),
   0
)
```

## Repository Structure

```
building-basics/          # Core building documentation
interactive-studio/       # Tasks, triggers, effects
advanced-tooling/         # Function Effect scripting
how-to/                   # Step-by-step tutorials
building-competitions/    # Community events
skills/
  portals-building-guide/
    SKILL.md              # Claude Code skill file
```

## Contributing

Contributions are welcome! You can:

1. Improve the documentation in any `.md` file
2. Enhance the skill at `skills/portals-building-guide/SKILL.md`
3. Add new tutorials to the `how-to/` section

## Resources

- [Live GitBook Docs](https://prtls.gitbook.io/portals-building-guide)
- [Portals Platform](https://theportal.to)
- [Portals SDK for Iframes](https://portals-labs.github.io/portals-sdk/portals-sdk.js)

## License

MIT License - See [LICENSE](LICENSE) file.

---

**Built for the Portals community**
