using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Svrio: MonoBehaviour
{
    public GameObject pivotPoint;
    // public GameObject target; 
    [Range(-60, 60)]
    public float angle; // [-90, 90]

    private float radius;
    private float pX, pY, pZ;
    private float x, y, z;

    void Start() {
        pX = pivotPoint.transform.position.x;
        pY = pivotPoint.transform.position.y;
        pZ = pivotPoint.transform.position.z;
        
        radius = Vector3.Distance(pivotPoint.transform.position, transform.position);

    }

    void Update() {
        
        x = pX + Remap(angle, -60.0f, 60.0f, 0.5f, 0.1f);
        y = pY + (radius * Mathf.Cos(Mathf.Deg2Rad * angle));
        z = pZ + (radius * Mathf.Sin(Mathf.Deg2Rad * angle));

        transform.position = new Vector3(x, y, z);

    }


    float Remap (float value, float from1, float to1, float from2, float to2) {
        return (value - from1) / (to1 - from1) * (to2 - from2) + from2;
    }
}

