using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WrestleTargetScript : MonoBehaviour
{
    public GameObject pivotPoint;
    float rotAngle;

    // Start is called before the first frame update
    void Start() {
        
    }

    // Update is called once per frame
    void Update() {
        
        transform.RotateAround(pivotPoint.transform.position, new Vector3(1, 0, 0), 90);

    }
}
