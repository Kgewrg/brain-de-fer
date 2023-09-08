using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;

public class UserInterfaceSricpt : MonoBehaviour
{
    public static int P1_EggConStatus;
    public static int P2_EggConStatus;
    public GameObject conStatusMessage_container;
    // public TMP_Text P2_EGG_text;

    void Start() {
        conStatusMessage_container.SetActive(false);
    }

    void Update() {

        // Αν δεν έχει συνδεθεί η συσκευή, εμφανίζει το text
        if (P1_EggConStatus == 0){
            conStatusMessage_container.SetActive(true);
        }else{
            conStatusMessage_container.SetActive(false);

        }

        // Gia 2 paixtes
        // if ((P1_EggConStatus == 0) || P2_EggConStatus == 0){
        //     conStatusMessage_container.SetActive(true);
        // }else{
        //     conStatusMessage_container.SetActive(false);

        // }
                      
    }
}
