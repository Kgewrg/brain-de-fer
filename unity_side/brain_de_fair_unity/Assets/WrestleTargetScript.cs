using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WrestleTargetScript : MonoBehaviour
{
    public GameObject pivotPoint;
    // public GameObject target; 
<<<<<<< HEAD
    [Range(-60, 60)]
=======
    [Range(-80, 80)]
>>>>>>> ba8de21916320738785328920982708667b64a6e
    public float angle; // [-90, 90]

    private float radius;
    private float pY, pZ;
    private float x, y, z;

    void Start() {
        pY = pivotPoint.transform.position.y;
        pZ = pivotPoint.transform.position.z;
        
        radius = Vector3.Distance(pivotPoint.transform.position, transform.position);
        
        
        
    }

    void Update() {
        x = transform.position.x;
        y = pY + (radius * Mathf.Cos(Mathf.Deg2Rad * angle));
        z = pZ + (radius * Mathf.Sin(Mathf.Deg2Rad * angle));

        transform.position = new Vector3(x, y, z);

<<<<<<< HEAD
=======




>>>>>>> ba8de21916320738785328920982708667b64a6e
        // transform.RotateAround(pivotPoint.transform.position, new Vector3(1, 0, 0), 90);

    }
}
