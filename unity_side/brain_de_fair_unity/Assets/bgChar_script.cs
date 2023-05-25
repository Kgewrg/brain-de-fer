using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgChar_script : MonoBehaviour
{

    public float jumpForce;
    private float ySpeed;

    public int activeAnim = 0; 

    [SerializeField] private Animator airPunchAnim; 
    [SerializeField] private string anim = "airPunch" ;
    
    // Start is called before the first frame update
    void Start() { 
        airPunchAnim.Play("idle", 0, 0.0f);        
    }

    // Update is called once per frame
    void Update() {
        if (activeAnim == 1){
            if (Input.GetKeyDown(KeyCode.Space)){   // θα γίνεται σε random
                // Debug.Log("Playing amin");
                airPunchAnim.Play(anim, 0, 0.0f);
            }           
        }
       
    }

    private void jump(){
        GetComponent<Rigidbody>().AddForce(Vector3.up * jumpForce);
    }
}
