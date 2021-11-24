# Service

## Exercises

*"When a significant process or transformation in the domain is not a natural responsibility of an ENTITY or VALUE OBJECT, add an operation to the model as standalone interface declared as a SERVICE. Define the interface in terms of the language of the model and make sure the operation name is part of the UBIQUITOUS LANGUAGE. Make the SERVICE stateless."*   Eric Evans Domain-Driven Design

### IoT plant watering

Reading the description of a simple computer controlled plant watering system at

<https://github.com/microsoft/IoT-For-Beginners/tree/main/2-farm/lessons/3-automated-plant-watering>


Make a note of the constants used in ```code-timing/server/app.py```

### Designing objects and services for the plant watering system

#### Problem statement

* We have sensors that measure soil moisture and temperature.

* We have actuators that control the watering systems.

* We wish to automatically water our plants.

* The watering needs of the plants is determined by the soil moisture and the plant development (height).

* There is a lag between watering the soil and the soil moisture measurement.

* There are preferred watering times - avoid midday on hot days.

* We require a *plant watering service*.

## Exercise 1

Create a glossary of the *domain language*.
Compare your glossary with the skeleton service in watering_service.py

## Exercise 2

Create outlines for the remaining classes required to implement a plant watering system.

## Reading

Read this article <https://www.ibm.com/garage/method/practices/code/domain-driven-design/>

## Resources

<http://gorodinski.com/blog/2012/04/14/services-in-domain-driven-design-ddd/>

<https://www.ibm.com/garage/method/practices/code/domain-driven-design/>

<https://www.cosmicpython.com/book/preface.html>