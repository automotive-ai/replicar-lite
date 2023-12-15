# replicar-lite

Our replicar-lite is designed to empower researchers and city planners with a versatile platform for traffic simulation and analysis. This library provides functionalities to simulate diverse traffic scenarios, enabling users to analyze, optimize, and evaluate traffic behaviors in various contexts.

## Features:
Naturalistic Nanoscopic Traffic Simulation: Naturalistic traffic simulation where each agent operates with its own independent decision-making process. Agents respond to their surroundings and configuration profiles, influencing their behavior in diverse scenarios.

Diverse Scenario Simulation: Generate and simulate traffic scenarios, including urban, highway, and customized maps with configurable traffic parameters.

Object-List Level Simulation: Simulate traffic at an object-list level, enabling low-fidelity testing for Advanced Driver Assistance Systems (ADAS) and Autonomous Driving (AD) functions.

Machine Learning Model Training: Train machine learning models for decision-making within autonomous systems using simulated traffic data.

City Planning Support: Design and analyze urban traffic scenarios to optimize traffic flow, identify congestion points, and refine infrastructure.

Compliance with Open Standards: Ensure compatibility and adherence to industry open standards such as ISO-34502, ASAM Open Drive, and Open Simulation Interface, facilitating seamless integration and interoperability.

## Getting Started:

### Installation:
1) Just clone the repo or extract the release package zip
2) Unzip libtensorflow.zip in the root folder of repo or extracted release

### Usage:
1) Add your_python_env/lib folder path to
   a) LD_LIBRARY_PATH env variable for Linux
   If not already present

2) Add the specific module that you want to use to the PYTHONPATH environment variable.
   For example, if you want to use the python3.6 package for Linux, you should run
   the following command from the root folder in the repository:

   export PYTHONPATH=$PYTHONPATH:./packages/python3.6/linux/aai

   This will make the module accessible to the interpreter

   Note:
   Please always use the matching interpreter version
   For instance, in the above example, the proper Python version should be python3.6

### License:
To be added
