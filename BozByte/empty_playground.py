import marimo as mo

# keep import in its own cell in your real notebook for faster init
app = mo.App()

@app.cell
def _():
    mo.md(" ")  # truly empty; renders an empty surface
    return

if __name__ == "__main__":
    app.run()
