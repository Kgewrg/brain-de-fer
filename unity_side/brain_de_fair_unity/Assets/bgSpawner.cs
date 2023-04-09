using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{
    
    public GameObject charPrefab;
    // Start is called before the first frame update
    void Start() {
        
        float sideDist = 1.5f;
        float heightOffset;
        int n_chars = 8;

        // First line (bot to top)
        for (int i = 0; i < n_chars; i++) {
            heightOffset = Random.Range(-1.0f, 1.0f);
            print(heightOffset);
            Instantiate(charPrefab, new Vector3((float)(-4.5 + (i*sideDist)), -2+heightOffset, 0), Quaternion.identity);
        }

        for (int i = 0; i < n_chars+1; i++) {
            heightOffset = Random.Range(-1.0f, 1.0f);
            Instantiate(charPrefab, new Vector3((float)(-5.5 + (i*sideDist)), 0+heightOffset, 0), Quaternion.identity);
        }

        for (int i = 0; i < n_chars; i++) {
            heightOffset = Random.Range(-1.0f, 1.0f);
            Instantiate(charPrefab, new Vector3((float)(-4.5 + (i*sideDist)), 2+heightOffset, 0), Quaternion.identity);
        }


        for (int i = 0; i < n_chars+1; i++) {
            heightOffset = Random.Range(-1.0f, 1.0f);
            Instantiate(charPrefab, new Vector3((float)(-5.5 + (i*sideDist)), 4+heightOffset, 0), Quaternion.identity);
        }
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
