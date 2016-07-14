Very SIMPLE piece of code I wrote over a few hours. Not having a ton of Python experience lately some of my time was looking at libraries for Mongo, understanding how python handles AbstractClasses, json processing and standing up the falcon library to accept routed REST requests quickly to play with.

The break down is 2 services (gateway, users) with common code that can be shared between services.

If I were to extend this (more time), I'd setup a configuraton system to store database locations and other pieces of config data each service might need.

I'd override the onGet falcon provides and handle custom request/respones.
