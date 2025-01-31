-- Join the 'start' and 'end' activities:

-- For each machine and process pair (machine_id, process_id), we need to join the records with activity_type = 'start' and activity_type = 'end' to get the corresponding timestamps for each process.
-- Calculate the processing time:

-- For each pair of start and end timestamps, subtract the 'start' timestamp from the 'end' timestamp to get the processing time for that specific process.
-- Aggregate the results:

-- Group by machine_id and calculate the average of all processing times for each machine.
-- Return the result:

-- Round the average processing time to 3 decimal places and return the machine_id along with the computed processing_time.



SELECT 
    machine_id, 
    ROUND(AVG(end_timestamp - start_timestamp), 3) AS processing_time
FROM (
    SELECT 
        a.machine_id, 
        a.process_id, 
        a.timestamp AS start_timestamp,
        b.timestamp AS end_timestamp
    FROM 
        Activity a
    JOIN 
        Activity b 
    ON 
        a.machine_id = b.machine_id 
        AND a.process_id = b.process_id
        AND a.activity_type = 'start'
        AND b.activity_type = 'end'
) AS process_times
GROUP BY machine_id;
