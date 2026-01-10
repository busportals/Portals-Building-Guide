# Claude Code Skill for Portals Building

This folder contains a Claude Code skill that teaches AI assistants everything about building in Portals.

## Quick Install

```bash
npx skills-installer install @busportals/Portals-Building-Guide/portals-building-guide --client claude-code
```

## Manual Installation

**Windows:**
```bash
xcopy /E /I "skills\portals-building-guide" "%USERPROFILE%\.claude\skills\portals-building-guide"
```

**macOS/Linux:**
```bash
cp -r skills/portals-building-guide ~/.claude/skills/
```

## What the Skill Includes

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

## Verify Installation

```bash
npx skills-installer list
```

You should see `portals-building-guide` in the list.
