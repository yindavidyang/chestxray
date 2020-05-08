docker run \
  --interactive \
  --tty \
  --rm \
  --volume `pwd`:/jmeter \
  egaillardon/jmeter \
    --nongui \
    --testfile test.jmx \
    --logfile result.jtl \
    --reportatendofloadtests \
    --reportoutputfolder report
