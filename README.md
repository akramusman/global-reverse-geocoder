# Kuwait Nearest Spot API

This project is a FastAPI application that provides an API to find the nearest point or spot to a given set of coordinates in Kuwait. It utilizes external APIs to retrieve location data and serves as a useful tool for location-based services.

## Project Structure

```
kuwait-nearest-spot-api
├── src
│   ├── main.py          # Entry point of the FastAPI application
│   ├── api
│   │   └── nearest.py   # API endpoint implementation for finding the nearest spot
│   ├── services
│   │   └── locator.py   # Logic for locating the nearest spot
│   └── types
│       └── spot.py      # Data model for a spot
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kuwait-nearest-spot-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

Once the application is running, you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

- **Find Nearest Spot**
  - **Endpoint:** `/nearest`
  - **Method:** `GET`
  - **Query Parameters:**
    - `lat`: Latitude of the location (required)
    - `lon`: Longitude of the location (required)
  - **Response:** Returns the nearest spot based on the provided coordinates.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.