## Vibration Analysis Toolset (vibration-analysis-toolset)

A full stack project for the analysis of vibration data using time and frequency techniques, applied on both public dataset samples and simulated data.

- Developer: _Leonardo Franco de Godói_
- GitHub profile: _https://github.com/lfgodoi_
- Contact: _eng.leonardogodoi@gmail.com_

### Running the app directly

It is usually common to need to run the app directly using Python for development and testing purposes, without the need to use Docker, which will only be required for its automatic deployment.

_Navigate to the app directory._

    cd app

_Create a virtual environment._

    python3 -m venv venv

_Activate the virtual environment._

    source venv/bin/activate

_Update the Pip._

    pip install --upgrade pip

_Install the app dependencies._

    pip install -r requirements.txt

_Run the app._

    python main.py