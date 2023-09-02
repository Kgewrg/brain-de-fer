using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;

public class UserInterfaceSricpt : MonoBehaviour
{
    public static int P1_EggConStatus;
    public GameObject P1_EGG_obj;
    // public TMP_Text P2_EGG_text;

    void Start() {
        P1_EGG_obj.SetActive(false);
        

    }

    void Update() {
        if (P1_EggConStatus == 0){
            P1_EGG_obj.SetActive(true);
        }else{
            P1_EGG_obj.SetActive(false);

        }

        // Gia 2 paixtes
        // if ((P1_EggConStatus == 0) || P2_EggConStatus == 0){
        //     P1_EGG_obj.SetActive(true);
        // }else{
        //     P1_EGG_obj.SetActive(false);

        // }
                      
    }
}
