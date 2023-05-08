using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgChar_script : MonoBehaviour
{

    public float jumpForce;
    private float ySpeed;

    public int activeAnim = 0; 
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update() {
       if (Input.GetKeyDown(KeyCode.Space)){
        jump();
       }
    }

    private void jump(){
        GetComponent<Rigidbody>().AddForce(Vector3.up * jumpForce);
    }
}
