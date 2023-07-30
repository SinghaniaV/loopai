from fastapi import FastAPI
from starlette.responses import FileResponse
from crud import get_csv_file, trigger_report_gen

app = FastAPI()


@app.get('/trigger_report')
async def trigger_report():
    report_id = await trigger_report_gen()
    # todo return running while generation
    return {'report generated with report_id': {report_id}}


@app.get('/get_report/{report_id}')
async def get_report(report_id: str):
    file_location = get_csv_file(report_id)

    # Return the CSV file as a streaming response
    return FileResponse(file_location, media_type='application/octet-stream', filename=f'{report_id}.csv')
