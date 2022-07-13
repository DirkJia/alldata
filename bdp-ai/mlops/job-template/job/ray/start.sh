#!/bin/bash

export RAY_HOST='ray-header-'$KFJ_PIPELINE_NAME'-'$KFJ_TASK_ID
echo RAY_HOST $RAY_HOST

while getopts n:f:i: flag
do
  case "${flag}" in
      n) num_worker=${OPTARG};;
      f) command=${OPTARG};;
      i) initsh=${OPTARG};;
  esac
done

echo "num_worker:" $num_worker
echo "init file:" $initsh
echo "python command:" $command


echo -e "\n\n\n===================begin create ray cluster\n\n\n"
if [ $initsh ];then
  python /app/launcher.py --num_worker ${num_worker} --deal 'create' --init ${initsh}
else
  python /app/launcher.py --num_worker ${num_worker} --deal 'create'
fi
echo -e "\n\n\n===================begin run python file\n\n\n"

$command

if [ $? -ne 0 ]; then
    sleep 10
    echo "\n\n\nfailed"
    echo "===================begin delete ray cluster\n\n\n"
    python /app/launcher.py --num_worker ${num_worker} --deal 'delete'
    exit 1
else
    sleep 10
    echo "\n\n\nsucceed"
    echo "===================begin delete ray cluster\n\n\n"
    python /app/launcher.py --num_worker ${num_worker} --deal 'delete'
    exit 0
fi


