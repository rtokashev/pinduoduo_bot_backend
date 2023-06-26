import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        'src.server:app',
        workers=1,
        log_level='debug'
    )
