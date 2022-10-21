#! /usr/bin/bash
readonly WORKDIR=${WORKDIR:-$(pwd)}
readonly AGGREGATE=${WORKDIR}/aggregate.py
readonly OUTDIR=${WORKDIR}/data

for d in benchmarks/*; do
	if [[ "$d" != *"_benchmark"* ]]
	then
		echo "IGNORING $d"
		continue
	fi

	bench_name=${d##*/}
 	bench_out=$OUTDIR/$bench_name

	echo "Running $bench_name"

	# Make sure directory exist
	if [[ ! -d $bench_out ]]
	then 
		echo "CREATING DIR $bench_out"
		mkdir $bench_out
	fi
	# run benchmark
	pytest --benchmark-json tmp.json $d

	# Append results
	echo "APPENDING $bench_name"
	python $AGGREGATE tmp.json $bench_out/bench_data.json
	# Clean dir

	echo "CLEANING $bench_name"
	rm tmp.json
done
# Make sure list.json is up to date
echo "GENEREATING LIST.JSON"
python buildlist.py . > $OUTDIR/list.json
