using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WrestleTargetScript : MonoBehaviour
{
    public GameObject pivotPoint;
    // public GameObject target; 
    [Range(-80, 80)]
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


    }
}
