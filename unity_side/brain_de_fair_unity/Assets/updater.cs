using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class updater : MonoBehaviour
{
    private string filePath;
    
    
    // Start is called before the first frame update
    void Start() {
        filePath = Application.dataPath + "value.txt"; 
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
