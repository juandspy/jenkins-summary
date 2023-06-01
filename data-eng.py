import pandas as pd


pd.set_option("display.max_colwidth", None)


df = pd.read_csv(
    "results.csv",
    dtype={"name": str, "build": int, "result": str, "duration": int},
)

df["duration"] = df["duration"] / 60 / 100  # convert to minutes
df["success"] = df["result"] == "SUCCESS"  # create a boolean column with the successes
df.drop("result", inplace=True, axis=1)
df.drop("build", inplace=True, axis=1)

df = (
    df.groupby(["name"], as_index=False)
    .agg(
        min_duration=("duration", "min"),
        mean_duration=("duration", "mean"),
        max_duration=("duration", "max"),
        success=("success", "mean"),
        num_builds=("success", "count"),
    )
    .round(2)
)

df.to_csv("parsed.csv", index=False)
