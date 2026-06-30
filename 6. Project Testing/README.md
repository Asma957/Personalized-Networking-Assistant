# Project Testing

## Testing Framework
pytest — Unit testing for all backend services

## Test File Location
`5. Project Development Phase/backend/tests/test_services.py`

## Test Cases

### Event Analyzer Tests
- test_analyze_event_returns_dict
- test_analyze_event_has_required_keys
- test_analyze_event_themes_is_list
- test_analyze_event_not_empty

### Fact Checker Tests
- test_fact_check_returns_dict
- test_fact_check_has_required_keys
- test_fact_check_known_topic
- test_fact_check_source_url

### Topic Generator Tests
- test_generate_starters_returns_dict
- test_generate_starters_has_starters_key
- test_generate_starters_count
- test_generate_starters_not_empty

### History & Feedback Tests
- test_get_history_returns_list
- test_save_feedback_success
- test_save_feedback_thumbs_down

## How to Run Tests
```bash
cd backend
python -m pytest tests/ -v
```

## API Testing
FastAPI Swagger UI available at:
`http://127.0.0.1:8000/docs`

## Test Results
All 15 unit tests passed successfully ✅
