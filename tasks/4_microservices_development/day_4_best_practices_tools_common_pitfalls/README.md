# Hands-on tasks: microservices best practices

## Task 1: modifying an application to follow best practices
Browse to:

`tasks/5_microservices_development/day_4_best_practices/app_that_doesnt_follow_best_practices/`

analyze the application - which microservice best practices it doesn’t follow?

The areas for improvement are written in
`tasks/5_microservices_development/day_4_best_practices/app_that_doesnt_follow_best_practices/areas_for_improvement.txt`, but
**first try to figure them out on your own**.

Improve the application.

## Task 2: creating a Kibana dashboard
Browse to `tasks/5_microservices_development/day_4_best_practices/elk` and start Elastic Stack.

Create a dashboard in Kibana that shows the number of 404 errors in the logs.

First, use the simplest approach. What is the problem with it?

If you have time, improve it.

## Task 3: adding custom Prometheus metrics
In `tasks/5_microservices_development/day_4_best_practices/prometheus-grafana-application-metric`
you have received a simple application that allows to upload files.

Make the number of uploaded files available in Grafana via Prometheus.

