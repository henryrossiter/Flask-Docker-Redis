# Abhinav and Henry's Project

## Dataset

Microsoft Stock prices

## API Spec

Call: GET /price

Description: Gets all of MSFT's end of day prices.

Sample Output: 
```
{
    3-31-19: 119.81
    4-1-19: 119.99
    4-2-19: 119.86
}
```

Call: GET /price/<day>

Description: Gets MSFT's end of day price for specified <day>

Sample Output:
```
{
    3-31-19: 119.81
}
```

Call: GET /average/<endDay>

Description: Gets MSFT's 10 day moving average of trading volume ending on <endDay>

Sample Output:
```
{118.09}
```

Call: POST /price/<day>

Description: Posts user's objects of prices to the day specified

Sample Output:
```
{'price post successful.'}
```

Call: GET /std

Description: Gets the standard deviation of MSFT end-of-day prices.

Sample Output:
```
{2.51}
```

## Usage

Curl: 

```curl -v http://localhost:8082/std```

Python:

```
import requests

resp = requests.get('http://localhost:8082/std')
if resp.status_code != 200:
    raise ApiError('GET /std/ {}'.format(resp.status_code))
print('Standard deviation: {}'.format(resp.json()))
```

## Pricing

$5 monthly for unlimited API access.

