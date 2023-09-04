using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class lightController : MonoBehaviour
{
    public Light[] FG_Lights;
    public Light[] BG_Lights;

    public float BG_minIntensity = 0.5f;
    public float FG_maxIntensity = 9.0f;
    public float changeFactor = 1.01f; // κατα πόσο θα μειώνενονται/αυξάνονται τα  φώτα



    void Start() {
    }

    void Update() { 
        // Debug.Log(UserInterfaceSricpt.P1_EggConStatus+" "+ UserInterfaceSricpt.P2_EggConStatus);

        if (UserInterfaceSricpt.P1_EggConStatus == 1){

            if ( BG_Lights[0].intensity > BG_minIntensity){
                dimBackgroundLights();
            }
            if (FG_Lights[0].intensity < FG_maxIntensity){
                brightenForgroundLights();
            }
        }
    }


    public void dimBackgroundLights(){
        foreach (var light in BG_Lights){
            light.intensity /= changeFactor;
        }
    }

    public void brightenForgroundLights(){
        foreach (var light in FG_Lights){
            light.intensity *= changeFactor;
        }
    }

}
