import os
cur = os.path.dirname(os.path.abspath(__file__))
new = os.path.join(cur, "postgres-data")

tblsc_check = os.path.join(new, 'pg_tblspc')
twophase_check = os.path.join(new, 'pg_twophase')
stat_check = os.path.join(new, 'pg_stat')
snacpshots_check = os.path.join(new, 'pg_snapshots')
replslot_check = os.path.join(new, 'pg_replslot')
commit_ts_check = os.path.join(new, 'pg_commit_ts')

logical_mappings = os.path.join(new, 'pg_logical', 'mappings')
logical_snapshots = os.path.join(new, 'pg_logical', 'snapshots')
wal_archive = os.path.join(new, 'pg_wal', 'archive_status')


if not (os.path.isdir(tblsc_check)):
    os.makedirs(tblsc_check)

if not (os.path.isdir(twophase_check)):
    os.makedirs(twophase_check)

if not (os.path.isdir(stat_check)):
    os.makedirs(stat_check)

if not (os.path.isdir(snacpshots_check)):
    os.makedirs(snacpshots_check)

if not (os.path.isdir(replslot_check)):
    os.makedirs(replslot_check)

if not (os.path.isdir(commit_ts_check)):
    os.makedirs(commit_ts_check)
    
if not (os.path.isdir(logical_mappings)):
    os.makedirs(logical_mappings)
    
if not (os.path.isdir(logical_snapshots)):
    os.makedirs(logical_snapshots)
    
if not (os.path.isdir(wal_archive)):
    os.makedirs(wal_archive)

print("directories created")
