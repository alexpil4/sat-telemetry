# Satellite Monitoring API 🛰️

SAT Telemetry is a project that collects and analyzes telemetry data from satellites, with the goal of monitoring the performance and operation of a satellite in real-time. The system gathers data from onboard sensors, processes it, and masks certain sensitive information to provide useful insights to engineers for maintaining the satellite's operations and troubleshooting any issues.

## Features

- **Real-time monitoring**: View telemetry data from the satellite in real-time.
- **Data collection**: Collects various types of data from sensors and onboard systems.
- **Data masking**: Sensitive telemetry data is masked for privacy and security purposes.
- **Processing and analysis**: Analyzes data to detect anomalies or performance issues.
- **User interface**: Provides a graphical interface to visualize the data in an understandable way.

## Installation

To set up the project, follow these steps:

1. Install dependencies
Make sure you have Python 3.x installed, then install the required dependencies:

```bash
cd sat-telemetry
pip install -r requirements.txt
```

2. Run the project
After installing the dependencies, you can run the telemetry API with:
```bash
uvicorn app.main:app --reload
```

3. This application is made with FastAPI application that provides interactive API documentation in two formats:

- **Swagger UI** – Available at [`/swagger`](http://localhost:8000/swagger), ideal for a direct API ineraction.
- **ReDoc** – Available at [`/redoc`](http://localhost:8000/redoc), ideal for understanding the API specifications.

## Support

If you find this project helpful and would like to support its development, you can make a donation via PayPal:

[![Donate with PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=X8VJ3YCNH67W2)


