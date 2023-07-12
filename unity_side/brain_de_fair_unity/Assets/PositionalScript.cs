using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PositionalScript : MonoBehaviour
{
    // Start is called before the first frame update
    public Slider slider;
    public Transform StartAxis;
    public Transform Lose;
    public Transform Win;

    private void Start()
    {
        transform.localPosition = StartAxis.localPosition;
    }

    private void Update()
    {
        float t = slider.value / slider.maxValue;
        Vector3 targetPosition = Vector3.Lerp(Lose.localPosition, Win.localPosition, t);
        if(slider.value  >= slider.maxValue / 2)
            transform.localPosition = Vector3.Lerp(StartAxis.localPosition, targetPosition, t);
        else
            transform.localPosition = Vector3.Lerp(targetPosition , StartAxis.localPosition, t);
    }
}
