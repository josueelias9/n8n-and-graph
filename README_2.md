start the project with compose

```sh
docker compose --profile gpu-nvidia build
```

This command is for:

```sh
docker compose --profile gpu-nvidia up
```

(optional) use a template to start working

<img src="README images/readme-image-1.png" alt="alt text" width="600"/>

when you are done working, save your project

<img src="README images/readme-image-2.png" alt="alt text" width="600"/>

Just saving the workflow is ok, but it will only live on your comptuer. To push the workflow to github, go to `localhost:5801` and search for your workflow. Save it. Then you use your git tool to have control over the changes you have made.

<img src="README images/readme-image.png" alt="alt text" width="600"/>

delete everything once you are done

```sh
docker compose --profile gpu-nvidia down -v
```