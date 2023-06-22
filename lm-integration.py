from fastapi import FastAPI
import uvicorn
from typing import Any, Dict, AnyStr, List, Union


app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@app.post("/csx_audit/")
async def root(arbitrary_json: JSONStructure = None):
    return {"status": "success", "received_data": arbitrary_json}

if __name__=="__main__":
    uvicorn.run("lm-integration:app", reload=True, )
