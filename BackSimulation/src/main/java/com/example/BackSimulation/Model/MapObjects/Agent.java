package com.example.BackSimulation.Model.MapObjects;

import java.awt.*;

public class Agent extends MapObject{
    private State state;

    private String color;

    public Agent(int id, Point coords) {
        super(id, coords);
        state = new State();
        color = "red";
    }

    public Agent(int id, Point coords, State state, String algo) {
        super(id, coords);
        this.state = state;
        if(algo.equals("QL")){
            color = "red";
        }
        if(algo.equals("DQL")){
            color = "blue";
        }
    }

    public Agent() {
        super(0 ,new Point(1,1));
        state = new State();
        color = "red";
    }

    @Override
    public String toString() {
        return "Agent{" +
                "id=" + getId() +
                ", coords=" + getCoords() +
                "state=" + state +
                '}';
    }

    public String toJSONString() {
        String ret = "{" +
                "\"id\": " + getId() + "," +
                "\"color\": \"" + color + "\"," +
                "\"state\": " + state.toJSONString() +
                "}";
        return ret;
    }
}
