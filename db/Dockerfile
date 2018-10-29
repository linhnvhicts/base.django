FROM postgres
RUN mkdir /scripts
ADD scripts/pg_backup_rotated.sh /scripts/
ADD scripts/pg_backup.config /scripts/
# Add crontab file in the cron directory
ADD crontab /etc/cron.d/pg-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/pg-cron
RUN chmod +x /scripts/pg_backup_rotated.sh

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
RUN update-rc.d cron enable
CMD cron && docker-entrypoint.sh postgres