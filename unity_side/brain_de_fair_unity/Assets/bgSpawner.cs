using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{
    
    public GameObject charPrefab;
    // Start is called before the first frame update
    void Start() {

        for (int i = 0; i < 4; i++) {
            Instantiate(charPrefab, new Vector3((float)(-4.5 + (i*2.5)), -2, 0), Quaternion.identity);
        }

        for (int i = 0; i < 5; i++) {
            Instantiate(charPrefab, new Vector3((float)(-5.5 + (i*2.5)), 0, 0), Quaternion.identity);
        }

        for (int i = 0; i < 4; i++) {
            Instantiate(charPrefab, new Vector3((float)(-4.5 + (i*2.5)), 2, 0), Quaternion.identity);
        }


        for (int i = 0; i < 5; i++) {
            Instantiate(charPrefab, new Vector3((float)(-5.5 + (i*2.5)), 4, 0), Quaternion.identity);
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
