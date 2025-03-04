# Satellite Monitoring API 🛰️

![Demo GIF](https://media3.giphy.com/media/LByQRF0zWOAp7ymQ2Q/giphy.gif)


SAT Telemetry API is a system designed to simulate satellite telemetry for testing and development purposes. It provides an API to generate and process telemetry data, allowing developers to test their applications as if they were interacting with real satellite data.

## Features

- **Satellite simulation**: Generates simulated telemetry data for testing.
- **Real-time API**: Provides real-time telemetry data via API endpoints.
- **Data masking**: Simulated data can be masked for testing different scenarios.
- **Customizable data**: Configure different telemetry parameters to fit testing needs.
- **FastAPI-based**: Built with FastAPI for high performance and easy integration.

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


