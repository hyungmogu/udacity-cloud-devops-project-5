<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class ImageConvertController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return;
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        // convert image to target format

        // upload image to amazon s3
        // set time for it to be deleted after 15 minutes or 1 day (if this is only thing allowed)

        // return uploaded amazon s3 url back to user
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        return;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        return;
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        return;
    }
}
