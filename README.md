# OpenBrain 🧠✨

**OpenBrain** is an intelligent management interface designed specifically for **OpenClaw**. It transforms the local configuration experience into a modern, fluid, and visually stunning control panel.

## ✨ Key Features

- **SPA Architecture (Single Page Application)**: Instant navigation between sections without page reloads.
- **Metrics Dashboard**: Visualization of token activity, estimated cost, and usage by AI model (GPT-4, Claude, Llama, etc.).
- **Skill Management**: Activate and deactivate your installed skills with a single click.
- **Integrated JSON Editor**: Manage your `openclaw.json` file with validation and syntax highlighting.
- **Backup Control**: Create and manage comprehensive restoration points for your environment.
- **Dark/Light Mode**: Premium interface adaptable to your visual preferences.

## 🚀 Installation

You can install OpenBrain directly from the source code:

```bash
# Clone the repository
git clone https://github.com/your-username/openbrain.git
cd openbrain

# Install the package in editable mode
pip install -e .
```

## 🛠️ Usage

OpenBrain includes an extremely simple Command Line Interface (CLI):

### Start the Web Server
```bash
openbrain start
```
Then open your browser at `http://localhost:5050`.

### Check System Status
```bash
openbrain status
```

### Create a Manual Backup
```bash
openbrain backup
```

## 📁 Project Structure

- `openbrain/core.py`: Business logic (config, skills, backups, metrics).
- `openbrain/api.py`: FastAPI-based backend.
- `openbrain/templates.py`: User Interface (HTML/JS/Tailwind) with SPA architecture.
- `openbrain/cli.py`: Command Line Interface.

## 📄 License

This project is licensed under the MIT License.
