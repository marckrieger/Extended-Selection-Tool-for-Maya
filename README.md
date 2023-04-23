# Extended-Selection-Tool-for-Maya
Extended Selection Tool is a script for Autodesk Maya which contains extra functionality for selecting geometry similar to the "Group" node in SideFX Houdini.

(Tested with Maya 2023)

## Current functionality:

- ## Select by normals:
  You can set the desired direction and spread angle and matching faces are going to be selected. Using the formula ```cos (θ) = (A *B) / (||A|| ||B||)``` to calculate the angle between the desired direction vector set by the user and the normal vectors of each face in the geometry, the script selects every face which returns an angle equal or smaller than the spread angle set by the user.)

  ![screenshot1](https://user-images.githubusercontent.com/74256390/233833245-e5347b7b-0efa-4157-b27e-0acea6401db5.png)
  ![screenshot2](https://user-images.githubusercontent.com/74256390/233833250-158826af-b91d-4b4f-b78c-65b6820dc096.png)

## To-do:

- Select by bounding box
- Select by bounding object
- Select random
