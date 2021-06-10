# Install

Install from git repository
```bash
pip install git+https://github.com/zaghaghi/direct-json-import.git
```

# Use
With the following json in a file named `info.json`.
```json
{
    "name": "hamed",
    "lastname": "zaghaghi",
    "repos": [
        "https://github.com/zaghaghi/direct-json-import"
    ]
}
```

you can directly import it as follows
```python
import info

print(info.data)

# {'name': 'hamed', 'lastname': 'zaghaghi', 'repos': ['https://github.com/zaghaghi/direct-json-import']}
```

![](demo.gif)

