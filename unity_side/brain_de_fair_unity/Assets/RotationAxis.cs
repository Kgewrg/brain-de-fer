using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class RotationAxis : MonoBehaviour
{
 // Start is called before the first frame update
    public Slider slider;
    public Transform startPoint;
    public Transform minPoint;
    public Transform maxPoint;

    private void Start()
    {
        transform.rotation = startPoint.localRotation;
    }

    private void Update()
    {
        float t = slider.value / slider.maxValue;
        Quaternion targetRotation = Quaternion.Lerp(minPoint.localRotation, maxPoint.localRotation, t);
        if(slider.value  >= slider.maxValue / 2)
            transform.rotation = Quaternion.Lerp(startPoint.localRotation, targetRotation, t);
        else
            transform.rotation = Quaternion.Lerp(targetRotation , startPoint.localRotation, t);
    }
}
