using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class lightController : MonoBehaviour
{
    public Light[] FG_Lights;
    public Light[] BG_Lights;

    private float BG_minIntensity = 0.5f;


    void Start() {
        BG_minIntensity+=1;
    }

    void Update() { 
        if (Input.GetKeyDown(KeyCode.G)){
            dimLights();
        }
        if (Input.GetKeyDown(KeyCode.T)){
            brightenLights();
        }
    }


    public void dimLights(){
        foreach (var light in FG_Lights){
            light.intensity /= 2;
        }
    }

    public void brightenLights(){
        foreach (var light in FG_Lights){
            light.intensity *= 2;
        }
    }

}
