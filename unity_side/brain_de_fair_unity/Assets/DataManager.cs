using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DataManager : MonoBehaviour {
    
    public static DataManager instance {get; private set; }
    
    private void Awake(){
        if (instance != null){
             Debug.LogError("Found more than one DataManager in scene.");
        }
    }

}
