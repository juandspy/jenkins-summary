import jenkins
from dotenv import dotenv_values

from jobs import JOBS as MY_JOBS


env_vars = dotenv_values(".env")  # take environment variables from .env.

server = jenkins.Jenkins(
    "https://ci.int.devshift.net/",
    username="jdiazsua",
    password=env_vars["TOKEN"],
    timeout=None,
)

user = server.get_whoami()
version = server.get_version()
# print("Hello %s from Jenkins %s" % (user["fullName"], version))
# print(server.jobs_count())

jobs = server.get_jobs(view_name="insights")
# print(f"There are {len(jobs)} insights jobs.")
ccx_jobs = [job for job in jobs if any(my_job in job["name"] for my_job in MY_JOBS)]
# print(f"There are {len(ccx_jobs)} CCX jobs.")

print("name,build,result,duration")

for job in ccx_jobs:
    info = server.get_job_info(job["name"])
    builds = info['builds']
    for build in builds:
        build_info = server.get_build_info(job["name"], build['number'])
        
        job_name = job.get('name',"")
        build_number = build_info.get('number',"")
        build_result = build_info.get('result',"")
        build_duration = build_info.get('duration',"")
        print(f"{job_name},{build_number},{build_result},{build_duration}")
